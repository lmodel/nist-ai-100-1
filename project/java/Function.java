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
  A top-level AI RMF Core function. Each function organizes AI risk
management activities at the highest level. GOVERN applies across
all stages; MAP, MEASURE, and MANAGE apply to AI-system-specific
contexts and lifecycle stages.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Function extends NamedThingRMF {

  private String functionCode;
  private List<Category> categories;


}