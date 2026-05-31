package None;

/* metamodel_version: 1.11.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  An implementation of the AI RMF Functions, Categories, and
Subcategories for a specific setting or application based on the
requirements, risk tolerance, and resources of the user (§6).
Profiles may be use-case-specific, temporal (current or target),
or cross-sectoral.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfProfile extends NamedThing {

  private String profileType;
  private String currentState;
  private String targetState;
  private String sector;
  private List<Subcategory> addresses;


}