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
  A generic grouping for any identifiable AI RMF element.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class NamedThing  {

  private URI id;
  private String name;
  private String title;
  private String description;
  private List<URI> seeAlso;


}